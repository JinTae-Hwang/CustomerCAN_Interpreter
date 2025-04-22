class UDSService():
    '''UDS Service Variable Definition Start'''
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
    '''UDS Service Definition End'''


uds = UDSService()
reqService = ['10', '19', '14', '11']
for rs in reqService:
    print (uds.udsServiceID[rs], uds.udsServicePRC[rs], uds.udsServiceNRC['22'])