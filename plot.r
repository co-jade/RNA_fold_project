library(ggplot2)
library(dplyr)

input_file <- commandArgs(trailingOnly = TRUE)[1]
data <- read.csv(input_file, header = FALSE)
colnames(data) <- "Score"
data$Distance <- 0:19

plot <- ggplot(data, aes(x = Distance, y = Score)) +
  geom_line() +
  labs(title = paste("Interaction Profile -", basename(input_file)), x = "Distance", y = "Score")

out_dir <- "plots"
out_file <- file.path(out_dir, paste0("interaction_profile_", tools::file_path_sans_ext(basename(input_file)), ".png"))
ggsave(out_file, plot, width = 8, height = 6, dpi = 300)