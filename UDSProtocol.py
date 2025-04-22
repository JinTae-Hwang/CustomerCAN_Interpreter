class UDSProtocol():
    # UDS Service Variable Definition Start
    udsServiceID = {
            '10':'DiagnosticSessionControl', 
            '11':'ECUReset',
            '14':'ClearDiagnosticInformation', 
            '19':'ReadDTCInformation', 
            '22':'ReadDataByIdentifier', 
            '27':'SecurityAccess',
            '2E':'WriteDataByIdentifier',
            '31':'RoutineControl',
            '34':'RequestDownload',
            '35':'RequestUpload',
            '36':'TransferData',
            '37':'RequestTransferExit',
            '3E':'TesterPresent'
            }

    udsServicePRC = {
            '10':'50', 
            '11':'51',
            '14':'54', 
            '19':'59', 
            '22':'62', 
            '27':'67',
            '2E':'6E',
            '31':'71',
            '34':'74',
            '35':'75',
            '36':'76',
            '37':'77',
            '3E':'7E'
            }

    udsServiceNRC = {
            '10':'generalReject',
            '11':'serviceNotSupported',
            '12':'subFunctionNotSupported',
            '13':'incorrectMessageLengthOrInvalidFormat',
            '14':'responseTooLong',
            '21':'busyRepeatRequest',
            '22':'conditionNotCorrect',
            '24':'requestSequenceError',
            '31':'requestOutOfRange',
            '33':'securityAccessDenided',
            '35':'invalidKey',
            '36':'exceedNumberOfAttempts',
            '37':'requiredTimeDelayNotExpired',
            '70':'uploadDownloadNotAccepted',
            '71':'transferDataSuspended',
            '72':'generalProgrammingFailure',
            '73':'wrongBlockSequenceCounter',
            '78':'requestCorrectlyReceived-ResponsePending',
            '7E':'subFunctionNotSupportedInActiveSession',
            '7F':'serviceNotSupportedInActiveSession',
            '81':'rpmTooHigh',
            '82':'rpmTooLow',
            '83':'engineIsRunning',
            '84':'engineIsNotRunning',
            '85':'engineRunTimeTooLow'
            }

    udsServiceDID = {
            'F100':'ACUIdentificationDataIdentifier',
            'F102':'ACUAndSensorHardwareDataIdentifier',
            'F101':'ACUCodingCodeDataIdentifier',
            'F103':'ACUStatusDataIdentifier',
            'F17F':'Vehicle Type, Variant, Version',
            'F187':'VehicleManufacturerSparePartNumberDataIdentifier',
            'F18B':'ACUManufacturingDateDataIdentifer',
            'F18C':'ECUSerialNumberDataIdentifier',
            'F190':'VINDataIdentifier',
            'F191':'VehicleManufacturerSparePartNumberDataIdentifier',
            'F193':'SystemSupplierECUHardwareVersionNumberDataIdentifier',
            'F195':'SystemSupploerECUSoftwareVersionNumberDataIdentifier',
            'F197':'SystemNameOrEngineTypeDataIdentifier',
            'F1A0':'ACU S/W versionDataIdentifer',
            'F1A1':'ECUSupplierCodeDataIdentifier',
            'F1B0':'ECUSoftwareUNITnumberDataIdentifier',
            'F1B1':'ECUSoftwareUNIT1VersionDataIdentifier',
            'F1B2':'ECUSoftwareUNIT2VersionDataIdentifier',
            'F1C1':'ECUSoftwareUNIT1IVDDataIdentifier',
            'F1C2':'ECUSoftwareUNIT2IVDDataIdentifier',
            'F1EF':'LocalRXSWINDataIdentifier'
            }
    # UDS Service Definition End

class acuProtocol():
    def decodeB1762DTC(self, rawData):
        self.B1762FlagBit = [
                         ['CAN Bus-Off', 'CAN Timout EMS', 'CAN Timeout ABS/ESC', 'CAN Timeout SAS', 'CAN Timeout, CLU', 'CAN Timeout, OCS', 'Unknown Coding Code', 'T/M Info'],
                         ['DAB - 1st', 'DAB - 2nd', 'PAB - 1st', 'PAB - 2nd', 'F RPT Drv', 'F RPT Pass', 'F APT Drv', 'F APT Pass'],
                         ['F SAB Drv', 'F SAB Pass', 'R SAB Drv', 'R SAB Pass', 'F CAB Drv', 'F CAB Pass', 'KAB - Drv', 'KAB - Pass'],
                         ['FIS - Drv', 'FIS - Pass', 'F SIS Drv', 'F SIS Pass', 'R SIS Drv', 'R SIS Pass', 'F PSIS Drv', 'F PSIS Pass'], 
                         ['F Buckle Drv', 'F Buckle Pass', 'STPS Drv', 'STPS Pass', 'PAB On/Off Switch', 'Telltale Lamp', 'PAB On/Off Lamp', 'CAN Timeout 4WD'],
                         ['No EOL Coding Process', 'PAB Active Vent', 'R Center Airbag', 'R RPT Drv', 'R RPT Pass', 'R Buckle Drv', 'R Buckle Pass', 'R CAB Drv'],
                         ['R CAB Pass', 'FIS - Center', 'CAN Line Operating Voltage Unstable', 'Reserved', 'Ext. Device Operating Voltage Unstable', 'F Center Side Airbag', 'EOL coding Error - Operating Voltage Error', 'DAB Tether'],
                         ['DAB Active Vent', 'PAB - 3rd', 'F ALL Drv', 'F ALL Pass', 'R RPT 2nd Drv', 'R RPT 2nd Pass', 'F Seat Cushion Airbag Drv', 'F Seat Cushion Airbag Pass'],
                         ['Rear Safing Sensor Center', 'CAN Timeout e-Clutch', 'No VIN Number', 'Swivel Seat Sensor 2nd Drv', 'Swivel Seat Sensor 2nd Pass', 'Active Hood Hinge - Drv', 'Active Hood Hinge - Pass', 'Active Hood Latch CTR'],
                         ['G-PPS - Drv', 'G-PPS - Pass', 'P-PPS Drv', 'P-PPS Pass', 'R Buckle Sensor - 1st Cetner', 'R Buckle Sensor - 2nd Center', '3rd Row RPT - Drv', '3rd Row RPT - Pass']
                        ] 
                
        self.result = []
        self.occurrenceCounter = int(rawData[18:20])
        self.occurrenceTime = int(rawData[20:24], 16) *  5
        self.dataBytesLen = int(len(rawData[24:]) / 2)

        for i in range(self.dataBytesLen) :
                byteData = int(rawData[24+(i*2):24+(i*2+2)], 16)
                for bit_i in range(8) :
                     if (byteData & (1 << bit_i)) == 1 :
                          self.result.append(self.B1762FlagBit[i][bit_i])
        if self.result :
             return self.occurrenceCounter, self.occurrenceTime, self.result
        else :
             return self.occurrenceCounter, self.occurrenceTime, None
