import json 

def zip_to_json(in_file,out_file): 
    city_dict_list = []
    with open(in_file, 'r') as i_f:
        key_line = i_f.readline()

        # creates list of keys on first line and then
        # splits on '\t' and strips '\n'
        keys = [k.strip() for k in key_line.split('\t')]

        # first line read in already from file so this loop starts
        # on the second line which contains the values
        for values in i_f:
            # instantiates data dictionary
            data_dict= {}

            # zip function creates a tuple containing
            for k, v in zip(keys, values.split('\t')):
                data_dict[k] = v.strip()
            
            # adds dictionary with country, zip code, city, state, 
            # latitute, and longitude to list of city dicts
            city_dict_list.append(data_dict)

    # dumps city_dict_list into a json file
    with open(out_file, 'w', encoding='utf-8') as o_f:
        o_f.write(json.dumps(city_dict_list, indent=2))
        
    print(f"\n-----\n{len(city_dict_list)} zip codes exported to {out_file}\n-----\n")
  
input_filename = 'US.txt'
output_filename = 'us_zips.json'

if __name__ == "__main__":
    zip_to_json(input_filename, output_filename)