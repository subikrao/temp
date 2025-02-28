import pandas as pa
import requests as rq

# base_url= f'https://dev.azure.com/{organization}/{project}/_apis/pipelines/{pipelineId}/runs?api-version=7.1-preview.1'
# base_url = f'https://dev.azure.com/{organization}/{project}/_apis/pipelines?api-version=6.0-preview.1'

base_url = f'https://dev.azure.com/cat-aa/Cat%20OS%20Platform/_apis/pipelines?api-version=7.1-preview.1'

personal_access_token= "8AxhBg8ziHUXe1GCPP3f8E7x8jxBg0ov5C7TLiNyKCcRutysYUm0JQQJ99BBACAAAAAq259BAAASAZDO3keG"

def pipes():
    headers={
        'Content-Type': 'application/json',
        'Authorization': f'Basic {personal_access_token}'
    }
    response = rq.get(base_url, headers=headers)
    response.raise_for_status()
    # return response.json()['value']
    print("Response Headers:", response.headers)
    print("Response Content:", response.content)
    
    try:
        return response.json()['value']
    except ValueError:
        print("Error: Unable to parse JSON response")
        return []

def main():
    pipelines = pipes()
    # pipelines_content = [{'Pipeline name': p['name']} for p in pipelines]
    # df = pa.DataFrame(pipelines_content)
    # df.to_csv('pipelinenames.csv', index=False)
    # print("saved pipelines")


if __name__ == '__main__':
    main()


    # curl -u :<PAT> \ "https://dev.azure.com/{organization}/{project}/_apis/pipelines?api-version=6.0-preview.1"

#     curl -u :8AxhBg8ziHUXe1GCPP3f8E7x8jxBg0ov5C7TLiNyKCcRutysYUm0JQQJ99BBACAAAAAq259BAAASAZDO3keG \
#   https://dev.azure.com/cat-aa/Cat%20OS%20Platform/_apis/pipelines/2806/runs?api-version=7.1
