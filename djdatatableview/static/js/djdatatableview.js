var djdatatableview = (function(){
    function renderColumn( data, type, row, meta ) { return data; }

    function initialize(name, opts) {
        var els = $('#' + name);
        var options = djdatatableview.getOptions(els[0], opts)
        els.DataTable(options)
    }

    function getOptions(dtview, opts) {
        opts = opts || {}

        var columnOptions = getColumns(dtview, opts.columnOptions || []);

        var defaultOptions = {
            select: {
                selector:'td:not(:first-child)',
                style:    'os'
            }
        }

        var ajaxOptions = {}, dataOptions = {};

        ajaxOptions = {
            ajax: {
                url: dtview.attributes.getNamedItem('source-url').textContent,
                contentType: "application/json",
                headers: { 'X-CSRFToken': jQuery("[name=csrfmiddlewaretoken]").val() },
//                data: data || {},
                type: "GET"
            }
        }

        var newOpts = Object.assign(
            {},
            columnOptions,
            defaultOptions,
            ajaxOptions,
            dataOptions
        )



        return newOpts;
    }

    function getColumns(dtview, columnOptions){
        var columns = [], columnDefs = [];
        var columnCount = dtview.children[0].children[0].children.length;
        var indentityFunction = function (data) { return data }

        for (var i = 0; i < columnCount; i++) {
            var column = dtview.children[0].children[0].children[i]

            var render = indentityFunction;
            if (columnOptions.length > i)
                render = columnOptions[i].render;

            columns.push({ data: column.textContent })
            columnDefs.push({
                targets: i,
                className: 'text-center',
                render
            })
        }
        return {
            columnDefs,
            columns
        }
    }

    var api = {
        initialize,
        getOptions
    }
    return api;
})()
