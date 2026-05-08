import argparse, json, io
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
parser=argparse.ArgumentParser(); parser.add_argument('--service-account-json',required=True); parser.add_argument('--file-id',required=True); parser.add_argument('--output',required=True); args=parser.parse_args()
info=json.loads(args.service_account_json); creds=service_account.Credentials.from_service_account_info(info, scopes=['https://www.googleapis.com/auth/drive']); service=build('drive','v3',credentials=creds)
request=service.files().get_media(fileId=args.file_id)
with io.FileIO(args.output,'wb') as fh:
    downloader=MediaIoBaseDownload(fh,request); done=False
    while not done:
        status,done=downloader.next_chunk(); print('Downloading...')
print('Downloaded',args.output)
