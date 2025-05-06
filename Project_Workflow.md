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
   
  ```
