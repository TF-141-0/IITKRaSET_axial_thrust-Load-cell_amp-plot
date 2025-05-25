### Development of algo for Load cell for Horizontal Propulsion Test and get plot of axial Thrust 


```mermaid
flowchart TD
    LIP[Project Workflow] -->B
    B[LoadCell & HX711] --> C(ESP32 & Ard IDE)
    C --> D[Serial Monitor verification/Calibration]
    D --> F[Establishing wireless UD/HTTP connection to microcontroller]
    D --> G[Set COM port For SD card]
    F --> I(Array logging on Matlab)
    G --> H[Gen .csv/TXT for later analysis]
    I --> J(Gen .csv for later analysis)
LIP@{ shape: lin-proc}
    LIP2[System execution] --> LP
    LP[ Load Plate / Motor Mount ] --> |Applies Force|AF[ Load Cell ]
     AF -->|Converts force to small analog voltage|HX[HX711 Amplifier]
     HX -->|Amplifies and converts analog to digital|ESP[ ESP32 Microcontroller ]
     ESP -->|Reads digital data from HX711, sends via Serial|MT[ PC->MATLAB ]
     MT -->SX(Receives serial data, logs it, plots thrust vs time)
LIP2@{ shape: lin-proc}
  ```
