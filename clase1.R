mtcars


install.packages("tidyverse")

library(tidyverse)

mtcars %>%
  filter(disp == 160) %>% 
  select(mpg, cyl, disp, hp, drat, wt, qsec) %>% 
  mutate(suma = mpg + cyl)

x <-3
y <-3
z <-3
a <-3

sa = x+y+z+a
conjunto = c(1,2,3,45)
