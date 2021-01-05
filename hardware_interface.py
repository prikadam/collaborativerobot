@ -18,7 +18,7 @@ def __init__(self, hardware_controller):

    def message(self, pn, message):
        if message.channel == "mode":
            print("msg",message.message)
            #print("msg",message.message)
            self.hardware_controller.update_mode(message.message)

class HardwareController:
@@ -62,9 +62,12 @@ def process_serial(self):
                self.joint_angle = int(vals[1])
            elif vals[0] == "m":
                self.mode = int(vals[1])
                #print("Mode c:",self.mode)
            else:
                print(vals)
                if self.mode == 1:
                    print("Mode: Joint Angle")
                elif self.mode == 2:
                    print("Mode: End Effector")
                elif self.mode == 3:
                    print("Mode: Autonomous")
        self.ser.close()

    def publisher_callback(self, envelope, status):
@@ -75,7 +78,12 @@ def update_mode(self, mode):
        if self.old_mode != mode:
            self.mode = mode
            self.ser.write(str(mode).encode())
            #print("Mode p:", self.mode)
            if self.mode == 1:
                print("Mode: Joint Angle")
            elif self.mode == 2:
                print("Mode: End Effector")
            elif self.mode == 3:
                print("Mode: Autonomous")

if __name__ =="__main__":
    uuid = "tmfrasca"
