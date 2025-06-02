import gymnasium as gym
import time

# Crear el entorno Boxing en dificultad 1
env = gym.make("ALE/Boxing-v5", render_mode="human", difficulty=1)

# Reiniciar el entorno y obtener la primera observación
obs, info = env.reset()

done = False

# Loop del juego
while not done:
    # Elegir una acción aleatoria
    action = env.action_space.sample()

    # Ejecutar la acción en el entorno
    obs, reward, terminated, truncated, info = env.step(action)

    # Mostrar info en consola (opcional)
    print(f"Reward: {reward}, Terminated: {terminated}, Truncated: {truncated}")

    # Pausar un poco para que se vea la animación
    time.sleep(0.02)

    # Condición de salida
    done = terminated or truncated

# Cerrar el entorno
env.close()
