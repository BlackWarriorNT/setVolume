import sys
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
import tkinter as tk

transparency = 0.75

def get_current_volume():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    return volume.GetMasterVolumeLevelScalar()

def set_volume(volume_percent):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volume.SetMasterVolumeLevelScalar(volume_percent / 100.0, None)

def adjust_volume(action):
    current_volume = get_current_volume()
    if action == "plus":
        new_volume = min(1.0, current_volume + 0.02)
    elif action == "minus":
        new_volume = max(0.0, current_volume - 0.02)
    else:
        print("Неверное значение. Используйте 'plus' или 'minus'.")
        sys.exit(1)
    set_volume(new_volume * 100)
    return new_volume * 100

def show_notification(message):
    root = tk.Tk()
    root.attributes("-alpha", transparency)  # Полупрозрачное окно
    root.overrideredirect(1)  # Убираем рамку окна

    label = tk.Label(root, text=message, font=("Helvetica", 52, "bold"), bg="#0A0A2A", fg="white")
    label.pack(pady=0, padx=0)

    root.update_idletasks()  # Обновляем окно, чтобы получить его размеры
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))  # Центрируем окно

    def fade_out(alpha=transparency):
        if alpha > 0:
            alpha -= 0.2
            root.attributes("-alpha", alpha)
            root.after(15, fade_out, alpha)
        else:
            root.destroy()

    root.after(1500, fade_out)  # Начинаем плавное исчезновение через 1.5 секунды
    root.mainloop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Укажите громкость или действие ('plus' или 'minus').")
        sys.exit(1)

    action = sys.argv[1]
    if action in ["plus", "minus"]:
        new_volume = adjust_volume(action)
        show_notification(f"Громкость: {int(new_volume)}%")
    else:
        try:
            volume_percent = float(action)
            if volume_percent < 0 or volume_percent > 100:
                raise ValueError
        except ValueError:
            print("Громкость должна быть числом от 0 до 100.")
            sys.exit(1)

        set_volume(volume_percent)
        show_notification(f"Громкость: {int(volume_percent)}%")