clear all
close all
clc

W=(2*rand(5,3)-1)/10;

I = [4 2 -1;
     0.01 -1 3.5;
     0.01 2 0.01;
    -1 2.5 -2;
    5 2 1.5];

T= [1 0 0;  %ssak
    0 1 0;  %ptak
    0 0 1]; %ryba

alfa=0.01;
beta=1;
epoch=5;

model=train_funct(I,W,T,epoch,alfa,beta);

sample=[2; 0.01; 0.01; -1;5];
model'*sample
