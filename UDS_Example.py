from UDSProtocol import UDSProtocol, acuProtocol
import os, sys

aP = acuProtocol()

req_service_id = ''
req_service_text = ''

cwd = os.getcwd()
file_name = cwd + sys.argv[0]
target = open(file_name, 'r', encoding='UTF-8')

for data in target:
    if '07D2' in data :                                                                     # 요청 메시지 ID가 포함되어 있는지 점검검
        sorted_data = [data_split.strip() for data_split in data.split(':')]                # 데이터 분리
        if ('Req' in sorted_data[2] and len(sorted_data) > 3) :                             # 데이터에서 요청 메시지인지 점검
            req_service_id = sorted_data[3][6:8]
            req_service_text = UDSProtocol.udsServiceID[req_service_id]
            print(f'Req ID : {req_service_id},  and Req Text : {req_service_text}')
    if '07DA' in data :                                                                    # 회신 메시지 ID가 포함되어 있는지 점검검
        sorted_data = [data_split.strip() for data_split in data.split(':')]               # 데이터 분리
        if ('Res' in sorted_data[2] and len(sorted_data) > 3) :                            # 데이터에서 긍정 회신 메시지인지 점검
            if ((res_service_id := sorted_data[3][4:6]) == UDSProtocol.udsServicePRC[req_service_id]) :     # SID 추출 및 긍정 응답인지 점검
                print(f'Req ID : {req_service_id},  and Res PRC : Pass ({res_service_id})')                 
                if sorted_data[3][4:6] == '59' and sorted_data[3][8:14] == '976200' :       # 요청이 B176200 DTC 상세 정보 요청에 대한 회신인지 점검
                    (count, time, error_flag) = aP.decodeB1762DTC(sorted_data[3])           # 맞다면 Interpretation 시도
                    print('B176200 Occurrence Count = ', count, '\tOccurrence Time(Minutes) = ', time, '\nError Contents = ', error_flag)
            if ((res_service_id := sorted_data[3][4:6]) == '7F') :                          # 데이터에서 부정 회신 메시지인지 점검
                print(f'Req ID : {req_service_id},  and Res NRC Text : Fail ({UDSProtocol.udsServiceNRC[res_service_id]})')
                
