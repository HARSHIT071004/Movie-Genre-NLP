genre_map = {
    1: "drama",
    2: "comedy",
    3: "horror",
    4: "action",
    5: "thriller",
    6: "romance"
}

import pickle

# Save the mapping to a pickle file
with open("label_encoder.pkl", "wb") as f:
    pickle.dump(genre_map, f)

print("Genre mapping saved!")

