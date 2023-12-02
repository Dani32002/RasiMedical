package tortninjas.rasimedical.ms.recursos;

import java.util.List;

import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface AsignacionRepository extends MongoRepository<Asignacion, String> {

    public List<Asignacion> findByMedico(Long medico);

    public List<Asignacion> findByTipo(String tipo);

    public List<Asignacion> findByActivo(boolean activo);

    public List<Asignacion> findByTipoAndElemento(String Tipo, Long elemento);
    
}
