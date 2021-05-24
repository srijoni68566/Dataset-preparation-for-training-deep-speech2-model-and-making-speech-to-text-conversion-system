from jiwer import wer

ground_truth = "কুমিল্লার খাদি সারা দেশে পরিচিত"
hypothesis = "কুমিল্লার খাদে সারা দেশে পরিচিত"

error = wer(ground_truth, hypothesis)
error
