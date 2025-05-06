Development of algo for Load cell for Horizontal Propulsion Test and get plot of axial Thrust 


```mermaid
flowchart TD
    B[LoadCell & HX711] --> C(ESP32 & Ard IDE)
    A[BreadB & GPI0] --> C
    C --> D[Serial Monitor verification]
    D --> E(Read Serial Data in MATLAB)
    E --> F[serialport/FXN/MATLAB R2019b+]
    E --> G[Set COM port, baud rate]
    E --> H[Read data in loop]
    F --> I(Array logging time/force)
    G --> I
    H --> I
    I --> J(Gen .csv for later analysis)

    LP[ Load Plate / Motor Mount ] --> |Applies Force|AF[ Load Cell ]
     AF -->|Converts force to small analog voltage|HX[HX711 Amplifier]
     HX -->|Amplifies and converts analog to digital|ESP[ ESP32 Microcontroller ]
     ESP -->|Reads digital data from HX711, sends via Serial|MT[ PC (MATLAB) ]
     MT -->SX(Receives serial data, logs it, plots thrust vs time)
  ```
