using LinearAlgebra # stdlib
using Optimization, Zygote # 3rd party 
using OptimizationOptimJL: GradientDescent, ConjugateGradient
## define test problem 
N = 100
xstar = rand(N)
A = rand(N,N)
fact = svd(A)
singular_values = range(start=1, stop=10, length=N)
A = fact.U * diagm(singular_values) * fact.Vt
b = A*xstar + 0.1*randn(N);
##
f(x, p ) = 1/2 * sum((A*x - b).^ 2) # cost function the api expects parametes p to be second input
# one could also write any of the equivalent expressions but the one above 
# is computationall more efficient for this particular case
# f(x) = 1/2 * norm(A*x - b)^ 2
# f(x) = 1/2 * (A*x - b)' * (A*x-b)
# f(x) = 1/2* dot(A*x-b, A*x-b)

x0 = zeros(N)
prob = OptimizationProblem(
    OptimizationFunction(
        f, 
        AutoZygote()
    ), 
    x0
)

sol = solve(prob, 
    GradientDescent(
        alphaguess=InitialStatic(alpha=2/opnorm(A))
    );
    maxiters=10000, 
    # abstol=1e-8,
    reltol=1e-8
)

relErr = norm(sol.u - xstar) / norm(xstar)
@info "Relative Error (truth) = $relErr"
## recall there is noise so lets check against a standard linear solver 

uhat = A\b
relErr = norm(sol.u - uhat) / norm(uhat)
@info "Relative Error (backslash)= $relErr"

