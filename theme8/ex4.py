from functools import reduce

sensor_readings = [18.5, 22.0, 95.3, 102.1, 24.5, 88.0, -5.0, 105.4]

filtered_t = filter(lambda x: x > 90, sensor_readings)
maped_t = map(lambda x: x * 1.8 + 32, filtered_t)
reduced_t = reduce(lambda x,y: x + y, maped_t)

# print (reduced_t)


from functools import reduce

sensor_readings = [18.5, 22.0, 95.3, 102.1, 24.5, 88.0, -5.0, 105.4]

cheta = reduce(
    lambda c, b: c + b,
    map(
        lambda c: c * 1.8 + 32,
        filter(lambda c: c > 90.0, sensor_readings)
    )
)

print(cheta)