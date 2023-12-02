package tortninjas.rasimedical.ms.recursos;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.List;
import java.util.Optional;

import org.json.JSONArray;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("asignacion")
public class AsignacionController {

    private static String URL_USUARIOS = "http://127.0.0.1:8001";

    private static String URL_INVENTARIO = "http://127.0.0.1:8000";

    private static String URL_MEDICO = URL_USUARIOS + "/usuario/medico/";

    private static String URL_DISPOSITIVO = URL_INVENTARIO + "/inventario/dispositivo/";

    private static String URL_MEDICAMENTO = URL_INVENTARIO + "/inventario/medicamento/";

    private static String URL_INSUMO = URL_INVENTARIO + "/inventario/insumo/";

    @Autowired
    private AsignacionRepository asignacionRepository;

    @PostMapping
    @ResponseStatus(code = HttpStatus.CREATED)
    public Asignacion addAsignacion(@RequestBody Asignacion asignacion) throws IOException, URISyntaxException{
        if (checkElemento(asignacion) && checkMedico(asignacion)) {    
            return asignacionRepository.save(asignacion);
        }
        return null;
        //return asignacionRepository.save(asignacion);
        
    }

    @GetMapping(value = "/")
    @ResponseStatus(code = HttpStatus.OK)
    public List<Asignacion> getAll() {
        return asignacionRepository.findAll();
    } 

    @GetMapping(value = "/medico/{id}")
    @ResponseStatus(code = HttpStatus.OK)
    public List<Asignacion> getAllMedico(@PathVariable Long id) {
        return asignacionRepository.findByMedico(id);
    } 

    @GetMapping(value = "/tipo/{tipo}")
    @ResponseStatus(code = HttpStatus.OK)
    public List<Asignacion> getAllTipo(@PathVariable String tipo) {
        return asignacionRepository.findByTipo(tipo);
    } 

    @GetMapping(value = "/tipo/{tipo}/elemento/{id}")
    @ResponseStatus(code = HttpStatus.OK)
    public List<Asignacion> getAllTipoElemento(@PathVariable String tipo, @PathVariable Long id) {
        return asignacionRepository.findByTipoAndElemento(tipo, id);
    } 

    @GetMapping(value = "/activo/{activo}")
    @ResponseStatus(code = HttpStatus.OK)
    public List<Asignacion> getAllActivo(@PathVariable Boolean activo) {
        return asignacionRepository.findByActivo(activo);
    } 
    
    @GetMapping(value = "/{id}")
    @ResponseStatus(code = HttpStatus.OK)
    public Asignacion findOne(@PathVariable("id") String id) throws Exception {
        Optional<Asignacion> asignacion = asignacionRepository.findById(id);
        if (asignacion.isEmpty())
            throw new Exception("Entity doesn't exist");
        return asignacion.get();
    }

    @DeleteMapping(value = "/{id}")
    @ResponseStatus(code = HttpStatus.NO_CONTENT)
    public void delete(@PathVariable String id) throws Exception {
        Optional<Asignacion> asignacion = asignacionRepository.findById(id);
        if (asignacion.isEmpty())
            throw new Exception("Entity doesn't exist");
        asignacionRepository.deleteById(asignacion.get().getId());
    }

    @PutMapping(value = "/{id}")
    @ResponseStatus(code = HttpStatus.OK)
    public Asignacion update(@PathVariable String id, @RequestBody Asignacion asignacion) throws Exception {
        Optional<Asignacion> asignacionOG = asignacionRepository.findById(id);
        if (asignacionOG.isEmpty())
            throw new Exception("Entity doesn't exist");
        asignacion.setId(asignacionOG.get().getId());
        return asignacionRepository.save(asignacion);
    }


    public Boolean checkElemento(Asignacion asignacion) throws IOException, URISyntaxException {
        JSONArray json = peticion(asignacion.getTipo());
        for (int i = 0; i < json.length(); i++) {
            if ((json.getJSONObject(i).getInt("pk")) == asignacion.getElemento()) {
                return true;
            }
        }
        return false;
    }

    public Boolean checkMedico(Asignacion asignacion) throws IOException, URISyntaxException {
        JSONArray json = peticion("Medico");
        for (int i = 0; i < json.length(); i++) {
            if ((json.getJSONObject(i).getInt("pk")) == asignacion.getMedico()) {
                return true;
            }
        }
        return false;
    }

    public JSONArray peticion(String forma) throws IOException, URISyntaxException {
        String direccion = "";
        if (forma.equals("Medico")){
            direccion = URL_MEDICO;
        } else if (forma.equals("Dispositivo")) {
            direccion = URL_DISPOSITIVO;
        } else if (forma.equals("Insumo")) {
            direccion = URL_INSUMO;
        } else {
            direccion = URL_MEDICAMENTO;
        }
        URI uri = new URI(direccion);
        URL url = uri.toURL();
        HttpURLConnection con = (HttpURLConnection) url.openConnection();
        con.setRequestMethod("GET");
        con.setRequestProperty("Content-Type", "application/json");
        BufferedReader in = new BufferedReader(new InputStreamReader(con.getInputStream()));
        String inputLine;
        StringBuffer content = new StringBuffer();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }
        in.close();
        con.disconnect();
        String respuesta = content.toString();
        JSONArray json = new JSONArray(respuesta); 
        return json;
    }
}
