import json
import random
from operator import itemgetter


def seeddata():
    num = 1
    json_list = []
    for i in range(20):
        for j in range(20):
            event_exists = random.randint(0, 1)
            if event_exists:
                latitude = i - 2
                longitude = j - 2
                event_id = num
                num += 1
                num_tickets = random.randint(0, 10)
                ticket_prices = []
                if num_tickets > 0:
                    for k in range(num_tickets):
                        random_price = float(("{0:.2f}").format(random.uniform(10, 100)))
                        ticket_prices.append(random_price)
                json_data = {}
                json_data['coordinate'] = [latitude, longitude]
                json_data['event_id'] = str(event_id)
                json_data['ticket_prices'] = ticket_prices
                json_list.append(json_data)
    seed_data = json.dumps(json_list)
    return seed_data


def manhattan_distance(a, b, c, d):
    return (abs(c - a) + abs(d - b))


if __name__ == "__main__":
    string = raw_input("Please input Coordinates seperated by a comma:")
    input_data = seeddata()
    #print input_data
    user_latitude, user_longitude = string.strip().split(",")
    user_latitude, user_longitude = int(user_latitude), int(user_longitude)  # user position

    distance = dict()  # key will be event_id and value will be distance
    coordinate = dict()  # key will be event_id and value will be coordinate
    lowest_price = dict()  # key will be event_id and value will be lowest price

    json_raw = json.loads(input_data)
    min_dist_keys = []  # this list will store 5 least distant co-ordinates along with distance from User Location where there is an event with minimum ticket information

    # iterating through all the json objects

    for obj in json_raw:
        dist = manhattan_distance(user_latitude, user_longitude, obj['coordinate'][0], obj['coordinate'][1])
        distance[obj['event_id']] = dist
        coordinate[obj['event_id']] = obj['coordinate']

        if obj['ticket_prices']:  ##  Events with avaliable tickets will be shown
            lowest_price[obj['event_id']] = min(obj['ticket_prices'])
            if len(min_dist_keys) < 5:
                min_dist_keys.append([dist, lowest_price[obj['event_id']], obj['event_id']])
            else:
                min_dist_keys = sorted(min_dist_keys, key=itemgetter(0,1))
                if (dist < min_dist_keys[4][0]) or (
        dist == min_dist_keys[4][0] and lowest_price[obj['event_id']] < min_dist_keys[4][
    1]):  # new coordinate distance is lower or distance is same and minimum price is lower
                    min_dist_keys.pop()
                    min_dist_keys.append([dist,lowest_price[obj['event_id']], obj['event_id']])

    min_dist_keys = sorted(min_dist_keys, key=itemgetter(0,1))

    # printing Answer
    print "Closest Events to (" + str(user_latitude) + "," + str(user_longitude) + "):"
    for item in min_dist_keys:
        print "Event " + item[2] + " - $" + str(lowest_price[item[2]]) + ", Distance " + str(
            item[0])
        # print min_dist_keys
