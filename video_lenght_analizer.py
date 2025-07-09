# -*- coding: utf-8 -*-
import os
from moviepy.editor import VideoFileClip
import tkinter as tk
from tkinter import filedialog, messagebox


def format_duration(seconds):
    """Converte a duração de segundos para o formato HH:MM:SS."""
    if seconds is None:
        return "00:00:00"
    # Arredonda para o segundo mais próximo
    seconds = round(seconds)
    # Calcula horas, minutos e segundos
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    # Formata a string de saída
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"


def analyze_videos_in_directory(directory):
    """
    Analisa um diretório e seus subdiretórios em busca de arquivos de vídeo,
    imprime suas durações e resume os resultados.
    """
    # Lista de extensões de arquivo de vídeo comuns
    video_extensions = ('.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mpeg', '.mpg')

    # Contadores para o resumo
    longer_than_90s = 0
    shorter_or_equal_to_90s = 0
    total_files_found = 0

    print(f"Iniciando a varredura no diretório: {directory}\n")
    print("-" * 70)

    # Percorre o diretório e seus subdiretórios
    for root, _, files in os.walk(directory):
        for filename in files:
            # Verifica se o arquivo tem uma extensão de vídeo
            if filename.lower().endswith(video_extensions):
                file_path = os.path.join(root, filename)
                total_files_found += 1
                try:
                    # Usa um bloco 'with' para garantir que o recurso seja fechado
                    with VideoFileClip(file_path) as video:
                        duration = video.duration  # Duração em segundos

                    # Formata a duração para exibição
                    formatted_duration = format_duration(duration)
                    print(f"Arquivo: {file_path}")
                    print(f"Duração: {formatted_duration}\n")

                    # Atualiza os contadores
                    if duration > 90:
                        longer_than_90s += 1
                    else:
                        shorter_or_equal_to_90s += 1

                except Exception as e:
                    # Captura exceções que podem ocorrer ao processar um arquivo
                    print(f"Arquivo: {file_path}")
                    print(f"Não foi possível ler a duração. Erro: {e}\n")

    # Imprime o resumo final
    print("-" * 70)
    print("Análise Concluída!")
    print("-" * 70)
    print(f"Total de arquivos de vídeo encontrados: {total_files_found}")
    print(f"Arquivos com mais de 1m30s: {longer_than_90s}")
    print(f"Arquivos com 1m30s ou menos: {shorter_or_equal_to_90s}")
    print("-" * 70)

    # Exibe o resumo final em uma caixa de mensagem
    summary_message = (
        f"Análise Concluída!\n\n"
        f"Total de arquivos de vídeo encontrados: {total_files_found}\n"
        f"Arquivos com mais de 1m30s: {longer_than_90s}\n"
        f"Arquivos com 1m30s ou menos: {shorter_or_equal_to_90s}"
    )
    messagebox.showinfo("Resumo da Análise", summary_message)


def select_directory_and_run():
    """Abre uma janela para o usuário selecionar o diretório e inicia a análise."""
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter

    # Abre a caixa de diálogo para selecionar a pasta
    directory_path = filedialog.askdirectory(title="Selecione a pasta para analisar")

    if directory_path:
        analyze_videos_in_directory(directory_path)
    else:
        print("Nenhum diretório selecionado. O programa será encerrado.")
        messagebox.showwarning("Aviso", "Nenhum diretório foi selecionado.")


if __name__ == "__main__":
    # Inicia a aplicação
    select_directory_and_run()
