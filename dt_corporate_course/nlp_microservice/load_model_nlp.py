# import torch

# from text_classification import classifier, TEXT, model, device

"""## Гиперпараметры"""

# size_of_vocab = len(TEXT.vocab)
# embedding_dim = 300
# num_hidden_nodes = 32
# num_output_nodes = 1
# num_layers = 2
# bidirection = True
# dropout = 0.2
#
# model = classifier(size_of_vocab, embedding_dim, num_hidden_nodes,num_output_nodes, num_layers,
#                    bidirectional = True, dropout = dropout)


# def load_model_nlp():
#     model.load_state_dict(torch.load('model.pt'))
#     model.eval()
#     return model


if __name__ == '__main__':
    # print(load_model_nlp())
    # 1
    # 2
    # 3
    # 4
    # 5
    import requests  # импортируем модуль

    send = requests.get('https://int-emb-glove-de-wiki.s3.eu-central-1.amazonaws.com/vectors.txt')  # делаем запрос

    file = open(r'D:\Desctop\Corp_course\dt_corporate_course\Nlp-microservice\vectors.txt', 'w')  # создаем файл для записи результатов
    file.write(send.text)  # записываем результат
    file.close()
