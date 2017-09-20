one_person_logit <- "
data {
int<lower=0> J; //количество карточек
int<lower=0> A; // количество альтернатив (общее)
int<lower=0> K; //число колонок в матрицах
matrix[A, K] X; // матрица наблюдений
int<lower=0> id[A]; // индексы
vector[A] y; // ответы
}
parameters {
vector[K] gamma; //коэф регрессии для популяции
vector[K] tau; //ст. отклоение для коэф.

vector[K] beta[J]; //трехмерная матрица коэф. для карточек
real sigma; //ст. отклонение для индив. наблюдений
}
model {
vector[A] mu; // линейный предиктор
//априоры (стандартные из инструкции)
gamma ~ normal(0,5); // для регрессии
tau ~ cauchy(0,2.5);
sigma ~ gamma(2,0.1);

for(j in 1:J){
beta[j] ~ normal(gamma,tau); //групповые коэф
}

for(a in 1:A){
mu[a] = X[a] * beta[id[a]]; //compute the linear predictor using relevant group-level regression coefficients
}

//правдоподобие
y ~ normal(mu,sigma);
}
"
id_vec <- rep(1:7, each = 5)
y_vec <- rep(choice_data[[1]]$y, each = 5)

person_data_one <- list(J = n_cards,
                        A = n_alternatives * n_cards,
                        K = 10,
                        X = choice_data[[1]]$X,
                        id = id_vec,
                        y = y_vec)

Dso <- stan_model(model_code = one_person_logit)

fit1 <- stan(model_code = one_person_logit,
             data = person_data_one,
             iter = 1000, chains = 4)
