Development of algo for Load cell for Horizontal Propulsion Test and get plot of axial Thrust 

```mermaid
flowchart TD
    A[BreadB & GPI0] B[LoadC &  HX711]
    B --> C(ESP32-Ard IDE)
    A --> C
    C -- Yes --> D[Do this]
    C -- No --> E[Do that]
    D --> F[End]
    E --> F
