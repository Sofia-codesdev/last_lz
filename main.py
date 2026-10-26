import pyramid
import kettle

def main():
    # задание 4
    pyramid.calculate_frustum_volume()
    
    print("\n" + "="*30 + "\n")

    # задание 6
    kettle.check_kettles()

if __name__ == "__main__":
    main()