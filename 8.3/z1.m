function z = z1(yy)
global c sigma
z = exp( - 0.5 * ((yy - c(1))/sigma) ^ 2)/ sum(exp( - 0.5 * ((yy - c)/sigma) .^ 2));
end



function z = z3(yy)
global c sigma
z = exp( - 0.5 * ((yy - c(3))/sigma) ^ 2)/ sum(exp( - 0.5 * ((yy - c)/sigma)  .^ 2));
end

function z = z4(yy)
global c sigma
z = exp( - 0.5 * ((yy - c(4))/sigma) ^ 2)/ sum(exp( - 0.5 * ((yy - c)/sigma)  .^ 2));
end

