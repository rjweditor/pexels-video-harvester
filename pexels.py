import requests

def download_hd_resolution_video(api_key, search_query, per_page=5):
    headers = {
        'Authorization': api_key,
    }

    base_url = 'https://api.pexels.com/videos/search'
    params = {
        'query': search_query,
        'per_page': per_page
    }

    response = requests.get(base_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        for video in data['videos']:
            # Find the 'hd' resolution video file
            hd_resolution_video = next((v for v in video['video_files'] if v['quality'] == 'hd'), None)

            if hd_resolution_video:
                video_url = hd_resolution_video['link']
                video_data = requests.get(video_url).content

                # Save the video to your local directory
                with open(f"{search_query}_{video['id']}.mp4", 'wb') as file:
                    file.write(video_data)
                print(f"Downloaded: {video['id']}.mp4")
            else:
                print(f"No 'hd' resolution available for video ID: {video['id']}")
    else:
        print(f"Failed to fetch videos. Status code: {response.status_code}")

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'
search_query = 'ADD_KEYWORD_HERE'  # Replace with your desired search keyword

download_hd_resolution_video(api_key, search_query)
