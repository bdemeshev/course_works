all_person_logit <- "
data {
int<lower=0> N; //число индивидов
int<lower=0> J; //количество карточек
int<lower=0> A; // количество альтернатив (общее)
int<lower=0> K; //число колонок в матрицах
matrix[A, K] X[N]; // матрицы наблюдений
int<lower=0> id[A]; // индексы
vector[A] y[N]; // ответы
}
parameters {
vector[K] gamma[N]; //коэф регрессии для популяции
vector[K] tau[N]; //ст. отклоение для коэф.

vector[K] beta[J, N]; //трехмерная матрица коэф. для карточек
real sigma[N]; //ст. отклонение для индив. наблюдений
}
model {
matrix[A, N] mu; // линейный предиктор
  //априоры (стандартные из инструкции)
  for (n in 1:N){
  gamma[n] ~ normal(0,5); // для регрессии
  tau[n] ~ cauchy(0,2.5);
  sigma[n] ~ gamma(2,0.1);
  }

for (n in 1:N){
for(j in 1:J){
beta[j, n] ~ normal(gamma[n],tau[n]); //групповые коэф
}}

for(n in 1:N){
for(a in 1:A){
mu[a, n] = X[a, n] * beta[id[a], n]; //compute the linear predictor using relevant group-level regression coefficients
}}

//правдоподобие
for (n in 1:N){
y[n] ~ normal(mu[n],sigma[n]);
}}
"

Dso <- stan_model(model_code = all_person_logit)



person_data <- list(N = n_persons,
                    J = n_cards,
                    A = n_alternatives * n_cards,
                    K = 10,
                    )
