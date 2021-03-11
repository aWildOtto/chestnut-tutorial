# Use the following as you please wherever you please... but keep in mind how variables work with function importing!

ranked_showtimes = [1900, 2000, 1800, 2100, 1700, 1600, 2200, 2300, 1500, 1400, 1300, 1200]

# def makeDict(lst):
#     res_dct = {lst[i]: i+1 for i in range(len(lst))}
#     return res_dct
    
# ranked_showtimes_dict = makeDict(ranked_showtimes)

# print(ranked_showtimes_dict)
# write your function here

def movie_scheduling(movies, available_showtimes):
    # assert len(movies) <= len(available_showtimes) == True
    
    sorted_available_time = sorted(available_showtimes, key=ranked_showtimes.index)

    sorted_movie = sorted(movies)

    # print(sorted_available_time)

    schedule = []
    time_ind = 0
    for movie in sorted_movie:

        schedule.append((movie, sorted_available_time[time_ind]))
        time_ind += 1

    revert_schedule = sorted(schedule, key=lambda x: movies.index(x[0]))
    # print(schedule)
    # print(revert_schedule)
    return revert_schedule


# don't need to change this
# you can run your code in develop mode test it out
if __name__ == '__main__':
    result = []
    expected = [[(1, 1900), (2, 1700), (3, 1300)],
                [(10, 1800), (2, 2000), (20, 2100), (25, 1500), (1, 1900)]]
# [(10, 1900), (2, 2000), (20, 1800), (25, 2100), (1, 1500)]
    result.append(movie_scheduling([1, 2, 3], [1300, 1700, 1900]))
    result.append(
        movie_scheduling([10, 2, 20, 25, 1],
                         [2100, 1500, 1900, 1800, 2000, 1400]))

    for i in range(len(result)):
        assert result[i] == expected[
            i], "movie_scheduling should have returned {}, actually got {}".format(
                expected[i], result[i])
        print("movie_scheduling correctly returned: {}".format(expected[i]))
