calculacorrelacion.m
clear all
close all
clc
L=32; %tamaño del sistema
beta=0.9;
Sij=2*(rand(L,L)>0.5) -1;% Estado inicial al azar.
npre = 1e6; %cantidad de pasos para la pretermalización.
npasos = 5e4;%cantidad de copias del ensamble
%Pretermalización.
energiapre=zeros(npre+1,1);%para estudiar cuántos pasos necesitamos para pretermalizar
energiapre(1) = En(Sij);
for n=1:npre
[Rij, DE, DM]=ising2Dpaso(Sij);
h=rand();
a=min(1,exp(-beta*DE));
if h<a;
Sij=Rij;
energiapre(n+1)=energiapre(n)+DE;
else
energiapre(n+1)=energiapre(n);
end
end
%sampleo del sistema a T fija
energia=zeros(npasos+1,1);
magnet=zeros(npasos+1,1);
energia(1) = En(Sij);
magnet(1) = sum(sum(Sij));
for n=1:npasos
[Rij,DE,dM] = ising2Dpaso(Sij);
h=rand();
a=min(1,exp(-beta*DE));
if h<a
energia(n+1)=energia(n)+DE;
magnet(n+1)=magnet(n)+dM;
Sij=Rij;
else
energia(n+1)=energia(n);
magnet(n+1)=magnet(n);
end
if(mod(n,10) == 0) % el resto de dividir n con 10
imagesc(Sij);shading flat; % grafica
title(['T = ' num2str(1/beta) ' e = ' num2str(energia(n)/(L*L)) ' m = ' num2str(magnet(n)/(L*L))],'fontsize',12,'fontweight','b');
drawnow;
end
end
e=energia./(L*L);
em=sum(e)/length(e);
stde=sqrt(sum(e.^2)/length(e)-em^2);
19
m=magnet./(L*L);
mm=sum(m)/length(m);
stdm=sqrt(sum(m.^2)/length(m)-mm^2);
Corrp=zeros(1,16);%cálculo de correlación
for n=1:16
p=n;
[corr]=correlacion(Sij,p);
Corrp(n)=corr;
end
figure;
plot(Corrp,'.');
xlabel('Distancia (espaciamiento en la red)','fontsize',12,'FontName','Arial');
ylabel('C_l','fontsize',12,'FontName','Arial');
title(['T= ' num2str(1/beta)],'fontsize',12,'fontweight','b');
figure;
plot(energiapre,'.');
xlabel('Iteración','fontsize',12,'FontName','Arial');
ylabel('Energía','fontsize',12,'FontName','Arial');
function [corr]=correlacion(Sij,p)
corr=0;
L=length(Sij);
for i=1:L
for j=1:L
C=sum(Sij(i,j)*Sij(i,j+p-L*(j>L-p))+Sij(i,j)*Sij(i+p-L*(i>L-p),j));
corr = corr + C;
end
end
corr=corr/(2*L*L);
end
