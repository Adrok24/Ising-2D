clear all
close all
clc

L=32; %tamaño del sistema
npre = 5e5; %cantidad de pasos para la pretermalización.
npasos = 5e4;%cantidad de copias del ensamble

b1=0.0001:0.001:0.9;
b2=0.9:0.05:3;
beta=[b1 b2];
U=zeros(length(beta),1);
M=zeros(length(beta),1);
SE=zeros(length(beta),1);
SM=zeros(length(beta),1);

for r=1:length(beta)
    Sij=2*(rand(L,L)>0.5) -1;% Estado inicial al azar. Matriz cuyas componentes valen 1 o -1 indicando las dos proyecciones de espin.
    energiapre = En(Sij); %Calcula la energía del estado inicial al azar
    for n=1:npre %Pretermalización.
%El estado al azar no es representativo de la T del sistema. El estado atipico se va transformando en un estado de equilibrio del 
%sistema que corresponde a uno de los microestados más probables, compatible con la T.
    [Rij, DE, DM]=ising2Dpaso(Sij);%ising2Dpaso genera un nuevo elemento en la cadena de Markov
    h=rand();
    a=min(1,exp(-beta(r)*DE));
        if h<a;
        Sij=Rij;
        energiapre=energiapre+DE;
        end
    end
    energia=zeros(npasos+1,1);%guardará la energía de cada cambio aceptado
    magnet=zeros(npasos+1,1);%guardará la magnetización de cada cambio aceptado
    energia(1) = En(Sij);% La función En(Sij) calcula la energia con condiciones de contorno periódicas. Este paso calcula la energía del último estado obtenido en la pretermalización.
    magnet(1) = sum(sum(Sij)); % Magnetización del estado final de la pretermalización. Suma la proyeccion de todos los spines.

    for n=1:npasos %Sampleo del sistema a T fija: generar microestados compatibles con la T del sistema.
    [Rij,DE,dM] = ising2Dpaso(Sij);
    h=rand();
    a=min(1,exp(-beta(r)*DE));
        if h<a
        energia(n+1)=energia(n)+DE; % para cada paso actualizo energia
        magnet(n+1)=magnet(n)+dM; % magnetizacion que tenia n mas cuanto vario
        Sij=Rij;
        else
        energia(n+1)=energia(n);
        magnet(n+1)=magnet(n);
        end
    end

e=energia./(L*L);%energía por sitio de cada elemento del ensamble
em=sum(e)/length(e);%energia por sitio media muestral
stde=sqrt(sum(e.^2)/length(e)-em^2);%desvío estándar muestral de la energía
m=magnet./(L*L);%magnetización por sitio de cada elemento del ensamble
mm=sum(m)/length(m);%magnetizacion por sitio media muestral
stdm=sqrt(sum(m.^2)/length(m)-mm^2);%desvío estándar muestral de la magnetización

M(r)=mm;%magnetización media a cada T muestreada
U(r)=em;%energía media a cada T muestreada
SE(r)=stde;%fluctuación de la energía a cada T
SM(r)=stdm;%fluctuación de la magnetización a cada T
end

subplot(2,2,1)
plot(beta,M,'.');
xlabel('\beta');
ylabel('Magnetización media por sitio');
subplot(2,2,2)
plot(beta,U,'.');
xlabel('\beta');
ylabel('Energía media por sitio');
subplot(2,2,3)
plot(beta,SE,'.');
xlabel('\beta');
ylabel('Desvio estándar de la energia media por sitio');
subplot(2,2,4)
plot(beta,SM,'.');
xlabel('\beta');
ylabel('Desvio estándar de la magnetización media por sitio');



