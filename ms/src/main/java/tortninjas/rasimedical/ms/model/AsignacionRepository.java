package tortninjas.rasimedical.ms.model;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;

public interface AsignacionRepository extends MongoRepository<Asignacion, Long> {

    public List<Asignacion> findByMedico(Long medico);

    public List<Asignacion> findByTipo(String tipo);

    public List<Asignacion> findByActivo(boolean activo);

    public List<Asignacion> findByTipoAndElemento(String Tipo, Long elemento);
    
}
