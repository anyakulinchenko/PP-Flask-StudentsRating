from waitress import serve
import prog
serve(prog.app, host='0.0.0.0', port = 5000)