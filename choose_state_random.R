states <- state.x77
# colnames(states)
total.pop <- sum(states[ ,1])

set.seed(33100)
# sample states, weighting with percentage of the total population per state
sample(x = row.names(states), size = 1, prob = states[ ,1]/total.pop)

# I got New York, which was incredibly lucky because I
# can actually get that data. 

