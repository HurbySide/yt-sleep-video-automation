import argparse, json, os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
parser=argparse.ArgumentParser(); parser.add_argument('--service-account-json',required=True); parser.add_argument('--folder-id',required=True); parser.add_argument('--file',required=True); parser.add_argument('--mime-type',default='video/mp4'); parser.add_argument('--out-json',required=True); args=parser.parse_args()
info=json.loads(args.service_account_json); creds=service_account.Credentials.from_service_account_info(info, scopes=['https://www.googleapis.com/auth/drive']); service=build('drive','v3',credentials=creds)
metadata={'name':os.path.basename(args.file),'parents':[args.folder_id]}; media=MediaFileUpload(args.file,mimetype=args.mime_type,resumable=True)
created=service.files().create(body=metadata,media_body=media,fields='id,name,webViewLink,webContentLink').execute()
open(args.out_json,'w',encoding='utf-8').write(json.dumps(created,ensure_ascii=False,indent=2)); print(json.dumps(created,ensure_ascii=False,indent=2))
