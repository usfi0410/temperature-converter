print('=== Temperature Converter ===')

def convert_temperature(degrees, original_scale, target_scale):
    if original_scale == 'C':
        if degrees >= -273.15:
            if target_scale == 'C':
                new_degrees = degrees
            elif target_scale == 'F':
                new_degrees = degrees * 9 / 5 + 32
            elif target_scale == 'K':
                new_degrees = degrees + 273.15
            else:
                return 'The value must be C/F/K!'
        else:
            return 'Temperatures below absolute zero are prohibited!'
        return f'Result: {degrees:.2f} {original_scale}  = {new_degrees:.2f} {target_scale}'

    elif original_scale == 'F':
        if degrees >= -459.67:
            if target_scale == 'C':
                new_degrees = (degrees - 32) * 5 / 9
            elif target_scale == 'F':
                new_degrees = degrees
            elif target_scale == 'K':
                new_degrees = (degrees + 459.67) * 5 / 9
            else:
                return 'The value must be C/F/K!'
        else:
            return 'Temperatures below absolute zero are prohibited!'
        return f'Result: {degrees:.2f} {original_scale}  = {new_degrees:.2f} {target_scale}'

    elif original_scale == 'K':
        if degrees >= 0:
            if target_scale == 'C':
                new_degrees = degrees - 273.15
            elif target_scale == 'F':
                new_degrees = degrees * 9 / 5 - 459.67
            elif target_scale == 'K':
                new_degrees = degrees
            else:
                return 'The value must be C/F/K!'
        else:
            return 'Temperatures below absolute zero are prohibited!'
        return f'Result: {degrees:.2f} {original_scale}  = {new_degrees:.2f} {target_scale}'
    else:
        return 'The value must be C/F/K!'

def main():
    try:
        degrees = float(input('Enter temperature: '))
    except ValueError:
        return 'The degree value must be a number!'

    original_scale = input('From (C/F/K): ')
    target_scale = input('To (C/F/K): ')

    original_scale = original_scale.strip().upper()
    target_scale = target_scale.strip().upper()

    return convert_temperature(degrees, original_scale, target_scale)

while True:
    print(main())

    answer = input('Convert another temperature? ')
    if answer.lower() == 'no':
        break

