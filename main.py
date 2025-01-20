import os
import pandas as pd
import json

import requests

#API params
URL = "https://wave.webaim.org/api/request"
API_KEY = os.environ.get('WAVE_KEY')

#reading top webpage data into a 100-website long list to feed to api
data = pd.read_csv("tranco_12-10-24_01-08-25_1m/top-1m.csv")[:100]
data["full_domain"] = "https://" + data["domain"].astype(str)
top_1m_100 = data["full_domain"]

#unused api params
REPORT_TYPE = 1
USERAGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0"

#feeding params to api, 1 call per website in top_1m_100, commented out after use to not expend more credits from WAVE
# data_list = []
# for domain in top_1m_100:
#     parameters = {
#         "key": API_KEY,
#         "url": domain
#     }
    # response = requests.get(url=URL, params=parameters)
    # data_list.append(response.json())

#save data received from wave api to saved_data.json (result: russian characters broke this process, so saved print output manually in saved_data.txt then made a copy of it, saved_data_copy.txt, to further process)
# print(data_list)
# with open("saved_data.json", mode="w") as file:
#     json.dump(data_list, file, ensure_ascii=False, indent=4)

#saving data from saved_data_copy.txt to json format
#saved_data_copy.txt was in format [{'status': {'success': True, 'httpstatuscode': 200}, 'statistics': {'pagetitle': 'Google',... so used ctrl+f to find and replace all ' with "
# with open("Data_Copies/saved_data_copy.txt", mode="r", encoding="utf-8") as data_txt_file:
#     with open("Data_Copies/saved_data_copy.json", mode="w", encoding="utf-8") as data_json_file:
#         json.dump(json.loads(data_txt_file.read().replace("True", "true").replace("False", "false")), data_json_file, indent=4, sort_keys=False, ensure_ascii=False)

#checking what domains got saved and which didn't and why (result, some failed which means they weren't recorded and didn't use any credits
# with open("saved_data_copy.json", mode="r", encoding="utf-8") as json_file:
#     api_results = json.load(json_file)
#
# fail = []
# success = []
# count_fail = 0
# for dict_item in api_results:
#     if dict_item["status"]["success"]:
#         success.append(dict_item["statistics"]["pageurl"])
#     else:
#         count_fail += 1
# for domain in top_1m_100:
#     if domain not in success:
#         fail.append(domain)
# print(fail)
# print(f"failed domains count: {count_fail}")

#trying failed domains again (result: still unsucessful and after research I'm still not sure what the fix is so I will use the 101-128 domains)
# data_list = []
# for domain in fail:
#     parameters = {
#         "key": API_KEY,
#         "url": domain
#     }
#     response = requests.get(url=URL, params=parameters)
#     data_list.append(response.json())
#
# print(data_list)
# with open("saved_data_fail1.json", mode="w", encoding="utf-8") as json_fail1_file:
#     json.dump(data_list, json_fail_file1, ensure_ascii=False, indent=4, sort_keys=False)

#reading 101-128 top webpage data into a 28-website long list to feed to api (result: successfully saved results into json file, 6 domains failed. Will repeat process with top webpages 129-135)
#accidentally skipped index 100 and didn't realize until after all 100 credits were used
# data = pd.read_csv("tranco_12-10-24_01-08-25_1m/top-1m.csv")[101:129]
# data["full_domain"] = "https://" + data["domain"].astype(str)
# top_1m_next28 = data["full_domain"]
#
# next_28 = []
# for domain in top_1m_next28:
#     parameters = {
#         "key": API_KEY,
#         "url": domain
#     }
#     response = requests.get(url=URL, params=parameters)
#     next_28.append(response.json())
#
# print(next_28)
# with open("saved_data_2.json", mode="w", encoding="utf-8") as json_file2:
#     json.dump(next_28, json_file2, ensure_ascii=False, indent=4, sort_keys=False)

#reading 129-135 top webpage data into a 6-website long list to feed to api (result: successfully saved results into json file, 6 domains failed. Will repeat process with top webpages 129-135)
# data = pd.read_csv("tranco_12-10-24_01-08-25_1m/top-1m.csv")[129:135]
# data["full_domain"] = "https://" + data["domain"].astype(str)
# top_1m_next6 = data["full_domain"]
#
# next_6 = []
# for domain in top_1m_next6:
#     parameters = {
#         "key": API_KEY,
#         "url": domain
#     }
#     response = requests.get(url=URL, params=parameters)
#     next_6.append(response.json())
#
# print(next_6)
# with open("saved_data_3.json", mode="w", encoding="utf-8") as json_file3:
#     json.dump(next_6, json_file3, ensure_ascii=False, indent=4, sort_keys=False)

#reading 136 top webpage data into a 1-website long list to feed to api (result: successfully saved results into json file, 1 domain1 failed. Will repeat process with top webpage 137)
# data = pd.read_csv("tranco_12-10-24_01-08-25_1m/top-1m.csv")[136:137]
# data["full_domain"] = "https://" + data["domain"].astype(str)
# top_1m_next1 = data["full_domain"]
#
# next_1 = []
# for domain in top_1m_next1:
#     parameters = {
#         "key": API_KEY,
#         "url": domain
#     }
#     response = requests.get(url=URL, params=parameters)
#     next_1.append(response.json())
#
# print(next_1)
# with open("OG_Data_DONOTTOUCH/saved_data_4.json", mode="w", encoding="utf-8") as json_file4:
#     json.dump(next_1, json_file4, ensure_ascii=False, indent=4, sort_keys=False)

#have successfully saved 100 domains to 4 separate json files (OG_Data_DONOTTOUCH/saved_data.json, OG_Data_DONOTTOUCH/saved_data_2.json, OG_Data_DONOTTOUCH/saved_data_3.json, OG_Data_DONOTTOUCH/saved_data_4.json)
#made copies of each (Data_Copies/saved_data_copy.json, Data_Copies/saved_data_2_copy.json, Data_Copies/saved_data_3_copy.json, Data_Copies/saved_data_4_copy.json)
#now will combine into 1 json file with all 100 successes and number them with their original indices (new indices don't matter, will be assigned with pandas later and will sort by old indices)

#get json files as list
my_dir = "Data_Copies"
jsons = [f for f in os.listdir(my_dir ) if os.path.isfile(os.path.join(my_dir, f)) and f[-4:]=="json"]

#get top websites list 1-136 (just domains)
top_136_domains = pd.read_csv("tranco_12-10-24_01-08-25_1m/top-1m.csv")[:137]["domain"]

#save json files to 1 combined file with old indicies
#open/create new combined json file
#manual removed extra brackets/formatting
# with open("saved_data_combined.json", mode="w", encoding="utf-8") as json_file_combined:
#     #loop through each json file in the my_dir directory
#     for file in jsons:
#         #open to read and write each file in the my_dir directory
#         print(f"{my_dir}/{file}")
#         with open(f"{my_dir}/{file}", mode="r+", encoding="utf-8") as load_file:
#             #load the data from load_file into json_data
#             json_data = json.load(load_file)
#             # loop through each dict item in json_data
#             for dom_dict in json_data:
#                 if dom_dict["status"]["success"]:
#                     #the value for the new key "old_index" in dom_dict will be the index of top_136_domains if the domain name of top_136_domain and dom_dict match
#                     dom_dict["old_index"] = int(top_136_domains.index[top_136_domains == dom_dict["statistics"]["pageurl"][8:]][0])
#                     print(dom_dict["old_index"])
#             #dump edited data into json_file_combined
#             json.dump(json_data, json_file_combined, indent=4, sort_keys=False, ensure_ascii=False)
