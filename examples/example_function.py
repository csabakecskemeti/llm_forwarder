# Example of your_rag_function.py
def dummy_rag(messages):
    static_context = "use the following context to answer the question.\nContext:\nThe code is 556677\n"
    for i in range(len(messages) - 1, -1, -1):
        if messages[i]['role'] == 'user':
            messages[i]['content'] = messages[i]['content'] + static_context 
            break
    return messages
