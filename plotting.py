import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from statistics import median


def combine_guesses(strategy, threads):
    all_guesses = []
    for i in range(threads):
        FileStore = open(f"stored_objects/{strategy}.{i}.pickle", "rb")
        guesses = pickle.load(FileStore)
        FileStore.close()
        all_guesses.extend(guesses)

    FileStore = open(f"stored_objects/{strategy}.pickle", "wb")
    pickle.dump(all_guesses, FileStore)
    FileStore.close()


def plot_games(num_guesses, display_name=None):
    games_by_score = Counter(num_guesses)
    for i in range(101):
        if i not in games_by_score.keys():
            games_by_score[i] = 0
    games_by_score = dict(sorted(games_by_score.items(), key=lambda item: item[0]))
    if display_name:
        plt.plot(games_by_score.keys(), games_by_score.values(), label=display_name)
    else:
        plt.plot(games_by_score.keys(), games_by_score.values())


def plot_all_games(file_names, display_names):
    for file_name, display_name in zip(file_names, display_names):
        FileStore = open(f"stored_objects/{file_name}.pickle", "rb")
        guesses = pickle.load(FileStore)
        FileStore.close()
        plot_games(guesses, display_name)
    plt.xlabel("Number of Guesses")
    plt.ylabel("Number of Games")
    plt.legend(loc="upper left")


def plot_all_cdfs(file_names, display_names):
    for filename, display_name in zip(file_names, display_names):
        FileStore = open(f"stored_objects/{filename}.pickle", "rb")
        guesses = pickle.load(FileStore)
        FileStore.close()
        sns.kdeplot(data=guesses, cumulative=True, clip=(0, 101), label=display_name)
    plt.xlabel("Number of Guesses")
    plt.legend(loc="upper left")


#file_names = ["random", "hunt_target", "hunt_target_parity", "hunt_target_min_parity", "prob", "weighted_prob"]
#display_names = ["Random", "Hunt / Target", "Hunt / Target with Parity", "Hunt / Target with Minimum Length Parity", "Probabilistic", "Weighted Probabilistic"]
file_names = ["prob", "weighted_prob"]
display_names = ["Probabilistic", "Weighted Probabilistic"]
num = 6
#for strategy in file_names:
#    combine_guesses(strategy, 6)

#plot_all_games(file_names[:num], display_names[:num])
plot_all_cdfs(file_names[:num], display_names[:num])
plt.show()
