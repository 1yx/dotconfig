from i3pystatus import Status
import socket

status=Status()

white="#cccccc"
green="#99cc99"
red="#f27777"

status.register("clock",
  format="%a %-d %b %H:%M:%S",
)

if socket.gethostname() != "skullcanyon":
  status.register("battery",
    format="{status}/{consumption:.2f}W {percentage:.2f}% {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
      "DIS": "↓",
      "CHR": "↑",
      "FULL": "=",
    },
    color=white,
    full_color=white,
    charging_color=green,
    critical_color=red,
    not_present_color=white,
  )

status.register("network",
  interface="wlp3s0",
  format_up="{essid} {network_graph_recv}{bytes_recv:6.1f}KiB↘{bytes_sent:5.1f}KiB↗",
  start_color=green,
  end_color=red,
)

status.run()
