library(tidyverse)
library(ggplot2)
library(RColorBrewer)

library(tableone)
library(survival)
library(survey)

setwd("/media/davidfdr99/WD_NiGo/D4GEN-2023/")

parsed_df <- read_tsv(file = "parsed_output/01-All_Mollusca_parsed.tsv",
         col_names = FALSE, guess_max = Inf)[,1:23]

header <- c("year", "class", "order", "family", "genus", "scientific_name",
            "latitude", "longitude", "elevation", "depth", "taxon_key",
            "n_native", "n_pres", "n_vagabond", "n_class", "n_order",
            "n_family", "n_genus", "iucn_status", "max_temp", "min_temp",
            "mean_temp", "prec_sum_mean")
names(parsed_df) <- header

# Filtering out Data Deficient ----
parsed_df <- parsed_df[parsed_df$iucn_status != "DD",]

# Categorical latitude ----
parsed_df <- parsed_df %>%
  mutate(latitude_class = case_when(
    abs(latitude) < 23.44 ~ "Tropical",
    abs(latitude) > 23.44 ~ "Temperate/Polar"))

# Output here for ML ? ----



parsed_df <- parsed_df %>%
  mutate(iucn_bin = case_when(
    iucn_status == "EW" | iucn_status == "EX" | 
    iucn_status == "VU" | iucn_status == "EN" | iucn_status == "CR" | 
    iucn_status == "NT" | iucn_status == "LR/cd" | iucn_status == "LR/nt"  ~ 1,
    iucn_status == "LC" ~ 0))

table(parsed_df$iucn_bin)
# Final run: 62k LC vs. 16k approx.

# Table of higher taxonomic data
# Potential huge bias of overrepresentation of some species in set.
v1 <- c("class", "order")
T.v1 <- CreateTableOne(vars = v1, strata = "iucn_bin", data = parsed_df, test = FALSE)
tmp <- data.frame(print(T.v1)) # Un peu de la magie noire mais ça marche


v2 <- c("latitude_class")
T.v2 <- CreateTableOne(vars = v2, strata = "iucn_bin", data = parsed_df, test = FALSE)
tmp <- data.frame(print(T.v2)) # Un peu de la magie noire mais ça marche

v3 <- c("n_native")
T.v3 <- CreateTableOne(vars = v3, strata = "iucn_bin", data = parsed_df, test = FALSE)
tmp <- data.frame(print(T.v3)) # Un peu de la magie noire mais ça marche


# Multivariate analysis ----
One_Liners_df <- data.frame()

for (i in unique(parsed_df$taxon_key)) {
  temp <- parsed_df[parsed_df$taxon_key == i,]
  temp <- temp[nrow(temp),]
  One_Liners_df <- rbind(One_Liners_df, temp)
} # Somewhat slow (30 seconds)

# Dealing with outliers on some climatic data (WIP, not DRY)
# Min temperature
my_rows <- nrow(One_Liners_df)
sdev <- sd(One_Liners_df$min_temp, na.rm = TRUE)
mean_col <- mean(One_Liners_df$min_temp, na.rm = TRUE)
One_Liners_df <- 
  One_Liners_df[(abs(One_Liners_df$min_temp - rep(mean_col, nrow(One_Liners_df))) < 3*sdev),]

print(cat("Removed", (my_rows - nrow(One_Liners_df)), "lines."))


# Mean sum precipitation
my_rows <- nrow(One_Liners_df)
sdev <- sd(One_Liners_df$prec_sum_mean, na.rm = TRUE)
mean_col <- mean(One_Liners_df$prec_sum_mean, na.rm = TRUE)
One_Liners_df <- 
  One_Liners_df[(abs(One_Liners_df$prec_sum_mean - rep(mean_col, nrow(One_Liners_df))) < 3*sdev),]

print(cat("Removed", (my_rows - nrow(One_Liners_df)), "lines."))

One_Liners_df$iucn_bin <- as.factor(One_Liners_df$iucn_bin)

One_Liners_df <- One_Liners_df[!is.na(One_Liners_df$iucn_bin), ]

# Scatter plot with classes ----
ggplot(One_Liners_df, aes(x = prec_sum_mean, y = min_temp,
                          shape = iucn_bin,
                          colour = iucn_bin,
                          fill = iucn_bin)) +
  geom_point() +
  scale_shape_manual(values = c(0,1)) +
  # scale_colour_brewer(palette = "Set1") +
  theme_minimal() +
  ggtitle("Influence of climatic data\non species endangerment") +
  xlab("Cumulative yearly precipitation at localisation") +
  ylab("Minimal yearly temperature") +
  labs(
    shape = "Endangered",
    colour = "Endangered"
  )


# TODO survival tests and plots for species with enough timepoints (> 30y) ----
# Linear interpolation ?




