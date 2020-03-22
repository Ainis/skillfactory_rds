import numpy as np

def half_search(num, lbound, ubound, count):
  test = int((lbound + ubound)/2) + int((lbound + ubound)%2)
  c = count + 1
  if num > test:
    return half_search(num, test, ubound, c)
  elif num < test:
    return half_search(num, lbound, test, c)
  elif num == test:
    return c
  
def game_core_v3(number):
  return half_search(number, 0, 100, 0)
  
def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)
    
score_game(game_core_v3)
