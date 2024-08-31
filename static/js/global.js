document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.to-do-list').forEach(taskElement => {
      taskElement.addEventListener('click', function() {
        // Obter dados da tarefa
        const title = this.getAttribute('data-task-title');
        const description = this.getAttribute('data-task-description');
        const createdAt = this.getAttribute('data-task-created-at');
        
        // Preencher o modal com os dados
        document.getElementById('modal-task-title').textContent = title;
        document.getElementById('modal-task-description').textContent = description;
        document.getElementById('modal-task-created-at').textContent = createdAt;
        
        // Mostrar o modal
        var myModal = new bootstrap.Modal(document.getElementById('taskModal'));
        myModal.show();
      });
    });
  });
