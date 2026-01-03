from flask import Blueprint, flash, g, redirect, render_template, request, url_for
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint("notes", __name__)


@bp.route("/")
def index():
    db = get_db()
    notes = db.execute(
        "SELECT p.id, title, body, created, author_id, username"
        " FROM note p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()
    return render_template("notes/index.html", notes=notes)


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "INSERT INTO note (title, body, author_id) VALUES (?, ?, ?)",
                (title, body, g.user["id"]),
            )
            db.commit()
            return redirect(url_for("notes.index"))

    return render_template("notes/create.html")


def get_note(id, check_author=True):
    note = (
        get_db()
        .execute(
            "SELECT p.id, title, body, created, author_id, username"
            " FROM note p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if note is None:
        abort(404, f"Note id {id} doesn't exist.")

    if check_author and note["author_id"] != g.user["id"]:
        abort(403)

    return note


def get_note_id(id, check_author=False):
    note = (
        get_db()
        .execute(
            "SELECT p.id, title, body, created, author_id, username"
            " FROM note p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )

    if note is None:
        abort(404, f"Note id {id} doesn't exist.")

    if check_author and note["author_id"] != g.user["id"]:
        abort(403)

    return note


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    note = get_note_id(id)

    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None

        if not title:
            error = "Title is required."

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                "UPDATE note SET title = ?, body = ? WHERE id = ?", (title, body, id)
            )
            db.commit()
            return redirect(url_for("notes.index"))

    return render_template("notes/update.html", note=note)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    get_note_id(id)
    db = get_db()
    db.execute("DELETE FROM note WHERE id = ?", (id,))
    db.commit()
    return redirect(url_for("notes.index"))


@bp.route("/<int:id>", methods=("GET",))
@login_required
def view(id):
    note = get_note_id(id)
    return render_template("notes/view.html", note=note)
