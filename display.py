import read
import write
import operations


def displayLand():
    data = read.readfile()
    print("\t|----------------------------------------------------------------------------|")
    print("\t|Kitta no | name of city | direction of Land |  Anna | Price | Availability  |")
    print("\t|----------------------------------------------------------------------------|")

    for row in data:
        kitta_no = row[0]
        name_city = row[1]
        direction_land = row[2]
        land_anna = row[3]
        land_price = row[4]
        land_availability = row[5]

        print("\t|{:<9}{:<13}{:<19}{:<7}{:<13}{:<15}|".format(kitta_no, name_city, direction_land, land_anna, land_price, land_availability))
        print("\t|----------------------------------------------------------------------------|")

displayLand()