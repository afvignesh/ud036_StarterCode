import media
import fresh_tomatoes

#creating different instances of Movie class from media file...
transformers = media.Movie("Transformers",
                           "The noble Autobots and devious Decepticons, two intergalactic races of robots, crash-land on Earth in order to battle for the ultimate power source, AllSpark, whose location is held by Sam.",
                           "http://www.gstatic.com/tv/thumb/movieposters/159729/p159729_p_v8_ar.jpg",
                           "https://www.youtube.com/watch?v=KrUhwet0ngg")


transformers_two = media.Movie("Transformers: Revenge of the Fallen",
                           "Sam leaves the Autobots behind for a normal life. However, when his mind is filled with cryptic symbols, the Decepticons target him and he is dragged back into the Transformers' war.",
                           "http://www.gstatic.com/tv/thumb/movieposters/192847/p192847_p_v8_am.jpg",
                           "https://www.youtube.com/watch?v=uH3STHC63hU")

transformers_three = media.Movie("Transformers: Dark of the Moon",
                           "Sam Witwicky and the Autobots must unravel the secrets of a Cybertronian spacecraft hidden on the moon before the Decepticons can use it for their own evil schemes.",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcQA5ydza4Rar3DEOsd0Wc6wL-6gpIzwjPZzfpb2vLNYxFRgm3RB",
                           "https://www.youtube.com/watch?v=kHRf01Gjosk")

transformers_four = media.Movie("Transformers: Age of Extinction",
                           "The Autobots, a faction of robots from the planet Cybertron, are hunted down by an elite CIA black ops unit and a ruthless bounty hunter. They turn to a struggling inventor and his daughter for help.",
                           "http://t0.gstatic.com/images?q=tbn:ANd9GcQiog19jyNYJ3uTY5pPNBCaWcS-mfJ8HLBLd58sGwB-1FObtFYX",
                           "https://www.youtube.com/watch?v=dYDGqmxMZFI")

transformers_five = media.Movie("Transformers: The Last Knight",
                           "Humans are at war with the Transformers, and Optimus Prime is gone. The key to saving the future lies buried in the secrets of the past and the hidden history of Transformers on Earth. Now, it's up to the unlikely alliance of inventor Cade Yeager, Bumblebee, an English lord and an Oxford professor to save the world.",
                           "http://t1.gstatic.com/images?q=tbn:ANd9GcQfKnoR3RsDT6gq3eEHzvH4XCt0Fal6sHiMZ7M98eyTF3ahSAPJ",
                           "https://www.youtube.com/watch?v=R4nrFuJedyk")

transformers_six = media.Movie("Bumblebee: The Movie",
                           "On the run in the year 1987, Bumblebee the Autobot seeks refuge in a junkyard in a small California beach town. Charlie, on the brink of turning 18 years old and trying to find her place in the world, soon discovers the battle-scarred and broken Bumblebee. When Charlie revives him, she quickly learns that this is no ordinary yellow Volkswagen.",
                            "https://www.bioskoptoday.com/wp-content/uploads/2017/06/Transformers-6.jpg",
                           "https://www.youtube.com/watch?v=ier0kkKn6bs")

#creating an array of the instances we just created, so as to pass it as a parameterr to open_movies_page function.
movies_array = [transformers, transformers_two, transformers_three, transformers_four, transformers_five, transformers_six]

#Calling open_movies_page function from fresh_tomatoes file.
fresh_tomatoes.open_movies_page(movies_array)
