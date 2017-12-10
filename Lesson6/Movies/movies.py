#!/usr/bin/python
import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwiEoo-h-v7XAhUM2o8KHcqBCIMQjRwIBw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFile%3AToy_Story.jpg&psig=AOvVaw2ZQHd5HxsH8XgiWqXv3khu&ust=1512978497420278",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print(toy_story.storyline)

avatar = media.Movie("Avatar",
					 "A marine on an alien planet helps them save it from humans.",
					 "https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjOtNyI_P7XAhUY148KHWd-AP0QjRwIBw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFile%3AAvatar-Teaser-Poster.jpg&psig=AOvVaw1jBN4ydjrGhq_7BfQS_diB&ust=1512978977533051",
					 "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print(avatar.storyline)
# avatar.show_trailer()

school_of_rock = media.Movie("School of Rock", "A musician who makes a his students form a band","https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwityqXMgP_XAhUMuY8KHV4cDHEQjRwIBw&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FFile%3ASchool_of_Rock_Poster.jpg&psig=AOvVaw3ujujrrbYX4hpaXeWdtT1y&ust=1512980198259210",
	"https://www.youtube.com/watch?v=XCwy6lW5Ixc")

incredibles = media.Movie("Incredibles", "A family with superpowers","https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwj7jPyjgf_XAhVJvY8KHS37A4UQjRwIBw&url=https%3A%2F%2Fwww.amazon.com%2FIncredibles-24-36-Movie-Poster%2Fdp%2FB018PSWRCC&psig=AOvVaw2J8k-r63wCYMgwXzGcY9n7&ust=1512980368019004", "https://www.youtube.com/watch?v=eZbzbC9285I")

finding_nemo = media.Movie("Finding Nemo", "A dad fish swims through the entire ocean to look for his lost son", "https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjxyqTegf_XAhUGMo8KHaONBQEQjRwIBw&url=https%3A%2F%2Fwww.amazon.com%2FFinding-Nemo-Pixar-Poster-Regular%2Fdp%2FB004Z1LRBQ&psig=AOvVaw0J8OsOOUZ5b246gNyzOZdH&ust=1512980494411225", "https://www.youtube.com/watch?v=wZdpNglLbt8")

avengers = media.Movie("Avengers", "All superheroes come together to save the world from evil", "https://www.google.co.in/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwjxvtekgv_XAhXJrY8KHaqeCtEQjRwIBw&url=http%3A%2F%2Fmarvelheroes.wikia.com%2Fwiki%2FFile%3AAvengers-movie-poster-1.jpg&psig=AOvVaw37iLOSdbQM537GSplZnP70&ust=1512980652326456", "https://www.youtube.com/watch?v=eOrNdBpGMv8")

movies = [toy_story, avatar, school_of_rock, incredibles, finding_nemo,avengers]

fresh_tomatoes.open_movies_page(movies)