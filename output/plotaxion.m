A = load("axion1_cl_lensed.dat");
C = load("extraCDM_cl_lensed.dat");
L = load("planckLCDM_cl_lensed.dat");
AR = (A(:,2)-L(:,2))./L(:,2);
CR = (C(:,2)-L(:,2))./L(:,2);
subplot(3,1,1); semilogx(A(:,1),AR,C(:,1),CR);
xlim([2,2000])
ylim([-0.6,0.6])
legend('axion','cdm')