import cx_Freeze
import sys

cx_Freeze.setup(
	name="Main.py",
	version="0.5.5",
	options={"build_exe": {"packages": ["pygame","os","sys","random"],
						   "include_files":["SQ_L.png", "Frog_L.png","Frog_R.png","MP_0.png","MP_1.png",
                                                    "MP_2.png","MP_3.png","MP_4.png","MP_5.png","MP_6.png",
                                                    "MP_7.png","MP_8.png","MP_9.png","MP_10.png","MP_11.png",
                                                    "MP_12.png","MP_13.png","MP_14.png","roca.png","RT1.png",
                                                    "Roca punta Sangre.png","ArañitaFinal_L.png","ArañitaFinal_R.png","SQ_L.png",
                                                    "SQ_R.png","Frog_L.png","Frog_R.png","Corazon_Vida.png","Corazon_Vacio.png",
                                                    "Cueva.jpg","Titulo_Juego.png","cabeza_araña2.png","P_CARGA.png",
                                                    "C1.png","C2.png","C3.png","C4.png","C5.png","C6.png",
                                                    "C7.png","C8.png","Feliz_L.png","Feliz_R.png","VICTORIA.wav","mus_spider.wav","GolpeEnemigo.wav","DERROTA.wav"]}
		    },
	executables=[cx_Freeze.Executable("Main.py")]
)
