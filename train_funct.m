% TRAINING FUNCTION FOR ONE NEURON
function training = train_funct(I,W,T,epoch,alfa,beta)
    rng(0,"twister");
    for i = 1:epoch
        f=randi([1 size(I,2)]);
        dI=I(:,f);
        U=W'*dI;
        y=1/(1+exp(-beta*U));
        D=T-y;
        alfaI=I*alfa;
        dW=alfaI*D';
        W=W+dW;
    end
    training=W;
end