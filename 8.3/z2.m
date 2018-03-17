function z = z2(yy)
global c sigma
z = exp( - 0.5 * ((yy - c(2))/sigma) ^ 2)/sum(exp( - 0.5 * ((yy - c)/sigma)  .^ 2));
end